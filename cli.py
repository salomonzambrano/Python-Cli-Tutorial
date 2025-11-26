import json_manager
import click
@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Name', help='The first name of the user.')
@click.option('--lastname', prompt='Last Name', help='The last name of the user.')  
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail("the name and Lastname cannot be empty.")
    else:
        data = json_manager.read_json()
        new_id = len(data)+1
        new_user = {
            "id": new_id,
            "name": name,
            "lastname": lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"datos guardados con exito {new_user}!")



@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']}-{user['name']}-{user['lastname']}")

@cli.command()
@click.argument('id', type=int)
def user(id):
    data =json_manager.read_json()
    user = next((x for x in data if x['id'] == (id)), None)
    if user is None:
        print(f"El usuario con id {id} no existe")
    else:
        print(f"{user['id']}-{user['name']}-{user['lastname']}")

@cli.command()
@click.argument('id', type=int)
@click.option('--name', help='The new first name of the user.')
@click.option('--lastname', help='The new last name of the user.')
def update(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
           if name is not None:
                user['name'] = name            
           if lastname is not None:
                user['lastname'] = lastname    
        break
    json_manager.write_json(data)
    print(f"Usuario con id {id} actualizado con exito")

@cli.command()
@click.argument('id', type=int)
def delete(id):
    data =json_manager.read_json()
    user = next((x for x in data if x['id'] == (id)), None)
    if user is None:
        print(f"El usuario con id {id} no existe")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"Usuario con id {id} eliminado con exito")



if __name__ =='__main__':
    cli()
