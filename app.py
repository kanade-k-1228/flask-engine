from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# -------------------------------------
# {key:number, name:string, deadline:date, status:bool}[]
class DB:
    data =  []
    def read(self):
        return self.data
    def create(self,name,deadline,status):
        self.data.append({'name':name,'deadline':deadline,'status':status})
    def update(self,i,name,deadline,status):
        self.data[i]=[{'name':name,'deadline':deadline,'status':status}]
    def delete(self,i):
        self.data.pop(i)
db = DB()
# -------------------------------------

global_scope={'db':db}

def run_script(script):
    local_scope={'ret':''}
    exec(script,global_scope,local_scope)
    ret = local_scope.get('ret')
    global_scope.update(local_scope)
    return ret
    
@app.route('/')
def root():
    ret = ''
    with open('index.pyhp','r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            # Script
            if char == '{':
                # Read until }
                bcnt = 1
                script = ''
                while True:
                    char = file.read(1)
                    if char == '{':
                        bcnt += 1
                    if char == '}':
                        bcnt -= 1
                    if bcnt == 0:
                        break
                    script += char
                ret += run_script(script)
            else:
                ret += char
    return ret

@app.route('/', methods=['post'])
def register():
    type = request.form.get('type')
    name = request.form.get('name')
    deadline = request.form.get('deadline')
    print(request.form)
    if type == 'create' and name and deadline:
        print(f'Create:{name}:{deadline}')
        db.create(name,deadline,'False')
    return redirect(url_for('root'))
