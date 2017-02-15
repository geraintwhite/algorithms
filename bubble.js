var array = [7, 6, 9, 4, 8, 2, 1, 5, 3, 0];

for (var j = array.length - 1; j > 0; --j) {
    for (var i = 0; i < j; ++i) {
        if (array[i] > array[i+1]) {
            tmp = array[i];
            array[i] = array[i+1];
            array[i+1] = tmp;
        }
    }
}

console.log(array);
