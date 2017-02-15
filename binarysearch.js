function binarysearch(searchkey, lower, upper) {
    var currindex = Math.floor((lower + upper) / 2);

    if (lower > upper) {
        return null;
    } else if (array[currindex] < searchkey) {
        return binarysearch(searchkey, currindex + 1, upper);
    } else if (array[currindex] > searchkey) {
        return binarysearch(searchkey, lower, currindex - 1);
    } else {
        return currindex;
    }
}


var array = [1, 5, 28, 44, 49, 52, 61, 74, 76, 95];


console.log(binarysearch(44, 0, array.length - 1));
console.log(binarysearch(76, 0, array.length - 1));
console.log(binarysearch(52, 0, array.length - 1));
console.log(binarysearch(99, 0, array.length - 1));
