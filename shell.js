var array = [7, 6, 9, 4, 8, 2, 1, 5, 3, 0];

var h = 1;

while (h <= array.length / 3) { h = h * 3 + 1 }
while (h > 0) { // h-sort the array
    for (var outer = h; outer < array.length; ++outer) {
        var temp = array[outer];
        var inner = outer;
        while (inner > h - 1 && array[inner - h] >= temp) {
            array[inner] = array[inner - h];
            inner = inner - h;
        }
        array[inner] = temp;
    }
    h = (h - 1) / 3;
}

console.log(array);
