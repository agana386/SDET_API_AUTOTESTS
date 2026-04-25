from models.entity import Post
import allure


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
        post = client.create_post(payload)

    with allure.step("Проверка данных"):
        assert post.title == payload["title"]
        assert post.body == payload["body"]
        assert post.userId == payload["userId"]


@allure.feature("GET API")
@allure.story("Get post")
@allure.title("Получение поста")
def test_get_post(client, created_post):
    with allure.step("Отправка GET запроса"):
        post = client.get_post(created_post.id)

    with allure.step("Проверка данных"):
        assert post.id == created_post.id


@allure.feature("Get all API")
@allure.story("Get all posts")
@allure.title("Получение всех постов")
def test_get_all_posts(client):
    with allure.step("Отправка GET запроса"):
        posts = client.get_all_posts()

    with allure.step("Проверка данных"):
        assert len(posts) > 0
        assert all(isinstance(post, Post) for post in posts)


@allure.feature("Patch API")
@allure.story("Change post")
@allure.title("Изменение поста")
def test_patch_post(client, created_post):
    payload = {"title": "updated title"}

    with allure.step("Отправка PATCH запроса"):
        post = client.patch_post(created_post.id, payload)

    with allure.step("Проверка данных"):
        assert post.title == payload["title"]


@allure.feature("Delete API")
@allure.story("Delete post")
@allure.title("Удаление поста")
def test_delete_post(client, created_post):
    with allure.step("Отправка DELETE запроса"):
        result = client.delete_post(created_post.id)

    with allure.step("Проверка пустого тела ответа"):
        assert result == {}