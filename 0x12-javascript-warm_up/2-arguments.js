#!/usr/bin/node
// Prints the message according to the no. of arguements

if (process.argv.length === 2) {
	console.log('No argument');
} else if (process.argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
