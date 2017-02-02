function Stack(length) {
    this.sp = 0;
    this.length = length;
    this.stack = new Array(length);
    this.push = function(data) {
        if (this.sp < this.length) {
            this.stack[this.sp] = data;
            this.sp++;
        } else {
            console.log('Stack Overflow');
        }
    };
    this.pop = function() {
        if (this.sp > 0) {
            this.sp--;
            console.log(this.stack[this.sp]);
        } else {
            console.log('Stack Empty');
        }
    };
}
