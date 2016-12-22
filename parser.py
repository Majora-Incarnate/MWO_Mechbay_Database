import json
import sys

def parse_to_json(source, target, blueprint):
	sourceFile = open('{0}.{1}'.format(blueprint['file'], source), 'r')

	sourceFile.readline()

	actuators = []

	for line in sourceFile:
		parts = line.split(';')

		actuator = {}

		for member, part in zip(blueprint['members'], parts):
			actuator[member] = part.rstrip()

		actuators.append(actuator)

	sourceFile.close()

	targetFile = open('{0}.{1}'.format(blueprint['file'], target), 'w')

	targetFile.write(json.dumps(actuators))

	targetFile.close()

def parse_to_csv(source, target, blueprint):
	sourceFile = open('{0}.{1}'.format(blueprint['file'], source), 'r')

	actuators = json.loads(sourceFile.read())

	sourceFile.close()

	targetFile = open('{0}.{1}'.format(blueprint['file'], target), 'w')

	targetFile.write(';'.join(blueprint['members']) + '\n')

	for actuator in actuators:
		parts = []

		for member in blueprint['members']:
			parts.append(actuator[member])

		targetFile.write(';'.join(parts) + '\n')

	targetFile.close()


def main():
	target = sys.argv[1]

	blueprintFile = open('definitions.json', 'r')

	blueprints = json.loads(blueprintFile.read())

	blueprintFile.close()

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