A=[7, 6, 9, 4, 8, 2, 1, 5, 3, 0]

for (var j = 2; j < A.length; ++j) {
    key = A[j];
    var i = j - 1;
    while (i >= 0 && A[i] > key) {
        A[i+1] = A[i];
        --i;
    }
    A[i+1] = key;
}

console.log(A);

