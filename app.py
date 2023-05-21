from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# -------------------------------------
class DB:
    data = [] # {name:string, deadline:yyyy-mm-dd}[]
    def read(self):
        return self.data
    def create(self,name,deadline):
        self.data.append({'name':name,'deadline':deadline})
    def update(self,index,name,deadline):
        self.data[index]=[{'name':name,'deadline':deadline}]
    def delete(self,index):
        self.data.pop(index)
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

@app.route('/create', methods=['post'])
def create():
    print(request.form)
    name = request.form.get('name')
    deadline = request.form.get('deadline')
    if name and deadline:
        print(f'Create:{name}:{deadline}')
        db.create(name,deadline)
    return redirect(url_for('root'))

@app.route('/delete', methods=['post'])
def delete():
    print(request.form)
    index = request.form.get('index')
    if index:
        print(f'Delete:{index}')
        db.delete(int(index))
    return redirect(url_for('root'))
