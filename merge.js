var array = [7, 6, 9, 4, 8, 2, 1, 5, 3, 0];
var workspace = new Array(array.length);


function mergesort(workspace, lower, upper) {
    if (lower == upper) return; // if range 1, done sorting

    var middle = Math.floor((lower + upper) / 2); // find midpoint

    mergesort(workspace, lower, middle); // sort lower half
    mergesort(workspace, middle + 1, upper); // sort upper half

    merge(workspace, lower, middle + 1, upper);
}

function merge(workspace, ptr1, ptr2, upper) {
    var j = 0;
    var lower = ptr1;
    var middle = ptr2 - 1;
    var n = upper - lower + 1; // number of items

    while (ptr1 <= middle && ptr2 <= upper) {
        if (array[ptr1] < array[ptr2]) {
            workspace[j++] = array[ptr1++];
        } else {
            workspace[j++] = array[ptr2++];
        }
    }

    while (ptr1 <= middle) {
        workspace[j++] = array[ptr1++];
    }

    while (ptr2 <= upper) {
        workspace[j++] = array[ptr2++];
    }

    for (var i = 0; i < n; ++i) {
        array[lower + i] = workspace[i];
    }
}


mergesort(workspace, 0, array.length - 1);

console.log(array);
