const obj = {
  x: 10,
  foo() {
    return this.x;
  },
};

console.log(obj.foo());
