const num = [-2, -1, 0, 1, 3, 4, 6, 9];

target = 8;

console.log(threesum(num, target));

function threesum(arr, target) {
	result = [];

	for (i = 0; i < arr.length; i++) {
		result.push(arr.slice(i), twosum(arr.slice(i), target - arr[i]));
	}
}

function twosum(arr, target) {
	for (i = 0; i < arr.length; i++) {
		if (arr.includes(target - arr[i])) {
			return [arr[i], target - arr[i]];
		}
	}
}
