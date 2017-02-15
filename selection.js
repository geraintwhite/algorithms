var array = [7, 6, 9, 4, 8, 2, 1, 5, 3, 0]

for (var i = 0; i < array.length - 1; ++i) {
    var min = i;
    for (var j = i + 1; j < array.length; ++j) {
        if (array[j] < array[min]) {
            min = j;
        }
    }
    var tmp = array[min];
    array[min] = array[i];
    array[i] = tmp;
}

console.log(array);
