function partition(left, right, pivot) {
    // call with left = 0, right = array.length - 1
    var leftPtr = left - 1;
    var rightPtr = right + 1;

    while (true) {
        while (leftPtr < right && array[++leftPtr] < pivot); // find bigger item
        while (rightPtr > left && array[--rightPtr] > pivot); // find smaller item

        if (leftPtr >= rightPtr) {
            break; // partition done
        } else {
            var tmp = array[leftPtr];
            array[leftPtr] = array[rightPtr];
            array[rightPtr] = tmp;
        }
    }

    return leftPtr; // return partition index
}


var array =  [51, 41, 6, 63, 86, 96, 57, 78, 22, 19];


console.log(partition(0, array.length - 1, 50), array);
