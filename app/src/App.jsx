import Slider from "./components/Slider";
import { io } from "socket.io-client";
import { useState } from "react";

const socket = io("http://localhost:80");

function App() {
  const [hue, setHue] = useState(0);
  const [brightness, setBrightness] = useState(0);

  function changeHue(value) {
    setHue(value);
    emitColor();
  }

  function changeBrightness(value) {
    setBrightness(value);
    emitColor();
  }

  function emitColor() {
    socket.emit("color", [hue, brightness]);
  }

  return (
    <div>
      <Slider
        value={hue}
        max={360}
        onInput={(value) => changeHue(value.target.value)}
      />
      <Slider
        value={brightness}
        className={"brightness"}
        max={100}
        onInput={(value) => changeBrightness(value.target.value)}
      />
      <div style={{ color: `hsl(${hue}, 100%, ${brightness}%)` }}>xd</div>
    </div>
  );
}

export default App;
