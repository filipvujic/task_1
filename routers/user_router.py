from fastapi import APIRouter
from services import user_service
from schemas.user import UserBase, UserUpdate

router = APIRouter(tags=["User"], prefix="/user")

@router.post("/create")
async def create(user: UserBase):
    return await user_service.create(user)

@router.get("/get-by-id/{id_param}")
async def get_by_id(id_param: str):
    return await user_service.get_by_id(id_param=id_param)

@router.patch("/update")
async def update(user: UserUpdate):
    return await user_service.update(user)

@router.delete("/delete-by-id/{id_param}")
async def delete_by_id(id_param: str):
    return await user_service.delete_by_id(id_param=id_param)


# # template_dir = os.path.join(os.path.dirname(__file__), 'pages')
# # jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
# #                                autoescape = True)

# file_loader = FileSystemLoader("pages")

# @router.patch("/update")
# async def home_page():
#     environment = jinja2.Environment(loader=file_loader)
#     template = environment.from_string("Hello, {{ name }}!")
#     #return template.render(name="World")
#     file_name = "index.html"
#     return environment.get_template("update_user.html", "w").render()
#     # with open(file_name) as f:
#     #     f.write(rendered)
#     # with open(f"{file_name}", "w") as f:
#     #     f.write(rendered)
