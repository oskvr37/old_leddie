// Create a new color picker instance
// https://iro.js.org/guide.html#getting-started
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


var colorPicker = new iro.ColorPicker(".colorPicker", {
  // Option guide: https://iro.js.org/guide.html#color-picker-options
  width: 300,
  color: "rgb(255, 0, 0)",
  borderWidth: 2,
  borderColor: "#fff"
});

colorPicker.on('input:end', function(color){
  setColor(color.hexString);
});

// handle click events on the swatch

var swatchGrid = document.getElementById('swatch-grid');

swatchGrid.addEventListener('click', function (e) {
  var clickTarget = e.target;
  // read data-color attribute
  if (clickTarget.dataset.color) {
    // update the color picker
    colorPicker.color.set(clickTarget.dataset.color);
    setColor(colorPicker.color.hexString);
  }
});
