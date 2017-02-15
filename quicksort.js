function quicksort(array, p, r) {
    if (p < r) {
        var q = partition(array, p, r);

        quicksort(array, p, q-1);
        quicksort(array, q+1, r);
    }
}


function partition(array, p, r) {
    var x = array[r];
    var i = p-1;

    for (var j = p; j < r; ++j) {
        if (array[j] <= x) {
            i = i + 1;
            var tmp = array[i];
            array[i] = array[j];
            array[j] = tmp;
        }
    }

    var tmp = array[i+1];
    array[i+1] = array[r];
    array[r] = tmp;

    return i + 1;
}


var array =  [51, 41, 6, 63, 86, 96, 57, 78, 22, 19];

quicksort(array, 0, array.length - 1);

console.log(array);
