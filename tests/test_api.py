from models.entity import Post
import allure

POST_ID = 1


@allure.feature("Posts API")
@allure.story("Create post")
@allure.title("Создание поста")
def test_create_post(client):
    payload = {
        "title": "test",
        "body": "test body",
        "userId": 1
    }

    with allure.step("Отправка POST запроса"):
        response = client.create_post(payload)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 201

    with allure.step("Десериализация ответа"):
        post = Post(**response.json())

    with allure.step("Проверка данных"):
        assert post.title == payload["title"]
        assert post.body == payload["body"]
        assert post.userId == payload["userId"]


@allure.feature("GET API")
@allure.story("Get post")
@allure.title("Получение поста")
def test_get_post(client):
    with allure.step("Отправка GET запроса"):
        response = client.get_post(POST_ID)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

    with allure.step("Десериализация ответа"):
        post = Post(**response.json())

    with allure.step("Проверка данных"):
        assert post.id == POST_ID


@allure.feature("Get all API")
@allure.story("Get all posts")
@allure.title("Получение всех постов")
def test_get_all_posts(client):
    with allure.step("Отправка GET запроса"):
        response = client.get_all_posts()

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

    with allure.step("Десериализация ответа"):
        posts = [Post(**item) for item in response.json()]

    with allure.step("Проверка данных"):
        assert len(posts) > 0


@allure.feature("Patch API")
@allure.story("Change post")
@allure.title("Изменение поста")
def test_patch_post(client):
    payload = {"title": "updated title"}

    with allure.step("Отправка PATCH запроса"):
        response = client.patch_post(POST_ID, payload)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

    with allure.step("Десериализация ответа"):
        post = Post(**response.json())

    with allure.step("Проверка данных"):
        assert post.title == payload["title"]


@allure.feature("Delete API")
@allure.story("Delete post")
@allure.title("Удаление поста")
def test_delete_post(client):
    with allure.step("Отправка DELETE запроса"):
        response = client.delete_post(POST_ID)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

    with allure.step("Проверка пустого тела ответа"):
        assert response.json() == {}