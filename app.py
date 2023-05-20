from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------------------
# {name:string, deadline:date, status:bool}[]
class DB:
    data =  [{'name':'item0','deadline':'item0-d','status':'item0-s'},
      {'name':'item1','deadline':'item1-d','status':'item1-s'}]
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
    if ret:
        return ret
    else:
        return ''

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
    get = {'name':request.form.get('name'),'deadline':request.form.get('deadline'),'status':request.form.get('status')}
    print(get)
    # if get not undefined:
    # db.create(get)
    return root()
