// Create a new color picker instance
// https://iro.js.org/guide.html#getting-started


var colorPicker = new iro.ColorPicker(".colorPicker", {
  // Option guide: https://iro.js.org/guide.html#color-picker-options
  width: 280,
  color: "rgb(255, 0, 0)",
  borderWidth: 1,
  borderColor: "#fff" });

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
