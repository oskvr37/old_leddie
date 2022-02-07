var colorPicker = new iro.ColorPicker('#picker', {
    layout: [
        { 
          component: iro.ui.Slider,
          options: {
            // can also be 'saturation', 'value', 'red', 'green', 'blue', 'alpha' or 'kelvin'
            sliderType: 'hue'
          }
        },
        { 
          component: iro.ui.Slider,
          options: {
            sliderType: 'value'
          }
        },
    ]
  });