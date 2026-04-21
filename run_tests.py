import pytest
import os
from datetime import datetime
from config.runtime import ACTUAL_STATUS

# Total esperado
TOTAL_CASES = 13
TOTAL_REQUIREMENTS = 6

# Mapeo de defectos
DEFECT_MAPPING = {
    "test_tc_10_post_invalid": "D-01",
    "test_tc_11_put_invalid": "D-02",
    "test_tc_12_patch_invalid": "D-03",
    "test_tc_13_delete_invalid": "D-04",
}

# Mapeo de requisitos
REQUIREMENT_MAPPING = {
    "test_tc_01_get_posts": "RF-1,RF-2",
    "test_tc_02_get_post_by_id": "RF-2,RF-3",
    "test_tc_03_get_post_comments": "RF-3",
    "test_tc_04_create_post": "RF-4",
    "test_tc_05_put_post": "RF-5",
    "test_tc_06_patch_post": "RF-5",
    "test_tc_07_delete_post": "RF-6",
    "test_tc_08_get_comments_by_post": "RF-3",
    "test_tc_09_get_post_invalid": "RF-3",
    "test_tc_10_post_invalid": "RF-4",
    "test_tc_11_put_invalid": "RF-5",
    "test_tc_12_patch_invalid": "RF-5",
    "test_tc_13_delete_invalid": "RF-6",
}


class ResultCollector:
    def __init__(self):
        self.passed = []
        self.failed = []

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            name = report.nodeid.split("::")[-1]

            if report.passed:
                self.passed.append(name)
            elif report.failed:
                self.failed.append(name)


def run():
    collector = ResultCollector()

    pytest.main(
        ["-q", "tests"],
        plugins=[collector]
    )

    total_executed = len(collector.passed) + len(collector.failed)
    passed = len(collector.passed)
    failed = len(collector.failed)

    passed_pct = (passed / TOTAL_CASES) * 100
    failed_pct = (failed / TOTAL_CASES) * 100

    # Defectos
    defects = []
    affected_requirements = set()

    for test in collector.failed:
        if test in DEFECT_MAPPING:
            defects.append(DEFECT_MAPPING[test])

        if test in REQUIREMENT_MAPPING:
            reqs = REQUIREMENT_MAPPING[test].split(",")
            affected_requirements.update(reqs)

    defect_count = len(defects)
    req_with_defects_count = len(affected_requirements)
    density = defect_count / req_with_defects_count if req_with_defects_count else 0

    # Construir salida
    output = []
    output.append("--- MÉTRICAS DE PRUEBAS ---\n")
    output.append(f"Fecha de ejecución: {datetime.now()}\n")

    output.append(f"Total casos ejecutados: {total_executed}")
    output.append(f"Casos pasados: {passed} ({passed_pct:.0f}%)")
    output.append(f"Casos fallidos: {failed} ({failed_pct:.0f}%)")
    output.append(f"Defectos encontrados: {defect_count}")
    output.append(f"Cobertura: {total_executed} / {TOTAL_CASES} casos\n")

    output.append("Requisitos con defectos:")
    for req in sorted(affected_requirements):
        output.append(f"- {req}")

    

    final_output = "\n".join(output)

    # Imprimir en consola
    print("\n" + final_output + "\n")

    # Guardar en archivo
    os.makedirs("evidence/latest", exist_ok=True)
    with open("evidence/latest/metrics.txt", "w") as f:
        f.write(final_output)

        # =========================
    # TABLA DE EJECUCIÓN (4.2)
    # =========================

    TEST_METADATA = {
        "test_tc_01_get_posts": ("GET /posts", "200"),
        "test_tc_02_get_post_by_id": ("GET /posts/1", "200"),
        "test_tc_03_get_post_comments": ("GET /posts/1/comments", "200"),
        "test_tc_04_create_post": ("POST /posts", "201"),
        "test_tc_05_put_post": ("PUT /posts/1", "200"),
        "test_tc_06_patch_post": ("PATCH /posts/1", "200"),
        "test_tc_07_delete_post": ("DELETE /posts/1", "200/204"),
        "test_tc_08_get_comments_by_post": ("GET /comments?postId=1", "200"),
        "test_tc_09_get_post_invalid": ("GET /posts/99999", "404"),
        "test_tc_10_post_invalid": ("POST /posts (invalid)", "400"),
        "test_tc_11_put_invalid": ("PUT /posts/99999", "404"),
        "test_tc_12_patch_invalid": ("PATCH /posts/99999", "404"),
        "test_tc_13_delete_invalid": ("DELETE /posts/99999", "404"),
    }

    execution_lines = []
    execution_lines.append(
        "ID | Descripción | Status Esperado | Status Obtenido | Resultado | Defecto"
    )
    execution_lines.append(
        "--------------------------------------------------------------------------"
    )

    ALL_TESTS = list(TEST_METADATA.keys())

    for test in ALL_TESTS:
        description, expected = TEST_METADATA[test]

        if test in collector.passed:
            result = "PASS"
        else:
            result = "FAIL"

        defect = DEFECT_MAPPING.get(test, "")
        actual = ACTUAL_STATUS.get(test, "N/A")

        execution_lines.append(
            f"{test} | {description} | {expected} | {actual} | {result} | {defect}"
        )

    execution_output = "\n".join(execution_lines)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")

    os.makedirs("evidence/history", exist_ok=True)
    with open(f"evidence/history/run_{timestamp}.txt", "w") as f:
        f.write(final_output + "\n\n" + execution_output)

if __name__ == "__main__":
    run()