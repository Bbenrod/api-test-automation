# Colección
GET_POSTS = "/posts"

# Recurso individual
GET_POST_BY_ID = "/posts/{id}"

# Relaciones (nested)
GET_POST_COMMENTS = "/posts/{id}/comments"

# Relaciones (filtro)
GET_COMMENTS_BY_POST = "/comments"

# CRUD
CREATE_POST = "/posts"
UPDATE_POST_PUT = "/posts/{id}"
UPDATE_POST_PATCH = "/posts/{id}"
DELETE_POST = "/posts/{id}"