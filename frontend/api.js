function setColor(hex) {
  console.log('set color to', hex);

  fetch("http://192.168.100.4:8000/color", {
    body: JSON.stringify({
      hex: hex
    }),
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
}
