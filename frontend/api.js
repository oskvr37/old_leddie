function setColor(rgb) {
  console.log('set color to', rgb);

  fetch("http://192.168.100.4:8000/color", {
    body: JSON.stringify({
      r: rgb.r,
      g: rgb.g,
      b: rgb.b,
    }),
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
}
