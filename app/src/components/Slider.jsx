import "./slider.css";

export default function Slider({ style, value, className, max, onInput }) {
  return (
    <div className="slider">
      <input
        type="range"
        min="0"
        max={max}
        value={value}
        onInput={onInput}
        style={style}
        className={className}
      ></input>
    </div>
  );
}
