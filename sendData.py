from flask import Flask,render_template
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

MACHINES = {
    'machine1': {'worktime': [1,2,3,4,9]}
}

def abort_if_machine_doesnt_exist(machine_id):
    if machine_id not in MACHINES:
        abort(404, message="Machine {} doesn't exist".format(machine_id))

parser = reqparse.RequestParser()
parser.add_argument('machine')

class Machine(Resource):
    def get(self, machine_id):
        abort_if_machine_doesnt_exist(machine_id)
        return MACHINES[machine_id]

    def delete(self, machine_id):
        abort_if_machine_doesnt_exist(machine_id)
        del MACHINES[machine_id]
        return '', 204

    def put(self, machine_id):
        args = parser.parse_args()
        worktime = {'worktime': args['worktime']}
        MACHINES[machine_id] = worktime
        return worktime, 201

# MachineList
# shows a list of all MACHINES, and lets you POST to add new worktimes
class MachineList(Resource):
    def get(self):
        return MACHINES

    def post(self):
        args = parser.parse_args()
        machine_id = int(max(MACHINES.keys()).lstrip('machine')) + 1
        machine_id = 'machine%i' % machine_id
        MACHINES[machine_id] = {'worktime': args['worktime']}
        return MACHINES[machine_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(MachineList, '/machines/')
api.add_resource(Machine, '/machines/<machine_id>')

@app.route('/')
def visualData():
    return render_template("showData.html")

if __name__ == '__main__':
    app.run(debug=True)