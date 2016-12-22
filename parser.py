import json
import sys

class Actuator:
	def __init__(self):
		self.file = 'actuator'
		self.members = ['name', 'id', 'section', 'index']

class Ammo:
	def __init__(self):
		self.file = 'ammo'
		self.members = ['name', 'id', 'tech base', 'artemis capable', 'apollo capable', 'health', 'criticals', 'tonnage', 'ammo type', 'shots', 'damage', 'cost']

class Armor:
	def __init__(self):
		self.file = 'armor'
		self.members = ['name', 'id', 'tech base', 'criticals', 'points per ton', 'armor per point', 'cost multiplier', 'upgrade multiplier']

class Chassis:
	def __init__(self):
		self.file = 'chassis'
		self.members = ['chassis', 'tech base', 'mech type', 'tonnage', 'movement archetype', 'description']

def parse_to_json(source, target, blueprint):
	sourceFile = open('{0}.{1}'.format(blueprint.file, source), 'r')

	sourceFile.readline()

	actuators = []

	for line in sourceFile:
		parts = line.split(';')

		actuator = {}

		for member, part in zip(blueprint.members, parts):
			actuator[member] = part.rstrip()

		actuators.append(actuator)

	sourceFile.close()

	targetFile = open('{0}.{1}'.format(blueprint.file, target), 'w')

	targetFile.write(json.dumps(actuators))

	targetFile.close()

def parse_to_csv(source, target, blueprint):
	sourceFile = open('{0}.{1}'.format(blueprint.file, source), 'r')

	actuators = json.loads(sourceFile.read())

	sourceFile.close()

	targetFile = open('{0}.{1}'.format(blueprint.file, target), 'w')

	targetFile.write(';'.join(blueprint.members) + '\n')

	for actuator in actuators:
		parts = []

		for member in blueprint.members:
			parts.append(actuator[member])

		targetFile.write(';'.join(parts) + '\n')

	targetFile.close()


def main():
	target = sys.argv[1]
	blueprints = [Actuator(), Ammo(), Armor(), Chassis()]

	if target == 'csv':
		source = 'json'

		for blueprint in blueprints:
			parse_to_csv(source, target, blueprint)
	elif target == 'json':
		source = 'csv'

		for blueprint in blueprints:
			parse_to_json(source, target, blueprint)
	else:
		return

if __name__ == "__main__":
	main()