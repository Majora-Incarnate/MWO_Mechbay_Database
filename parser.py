import json
import sys

def parse_to_master(blueprints):
	components = {}

	for blueprint in blueprints:
		with open('{0}.json'.format(blueprint['file']), 'r') as sourceFile:
			components[blueprint['file']] = json.loads(sourceFile.read())

	with open('master.json', 'w') as targetFile:
		targetFile.write(json.dumps(components))

def debug_log(debug, source, target, blueprint):
	if not debug:
		return

	print('source: {}'.format(source))
	print('target: {}'.format(target))
	print('blueprint: {}'.format(blueprint))

def main():
	if len(sys.argv) > 1 and sys.argv[1].lower() == 'debug':
		debug = True
	else:
		debug = False

	blueprints = []

	with open('definitions.json', 'r') as blueprintFile:
		blueprints = json.loads(blueprintFile.read())

	parse_to_master(blueprints)

if __name__ == "__main__":
	main()