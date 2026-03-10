# Animation

`src/css/utilities/animation.css`

Shorthand transition and scroll-driven animation utilities. Prefer these over writing `transition` or `animation` properties inline.



## Transitions

Apply `transition-all` with a fixed duration:

| Class                 | Transition                    |
| --------------------- | ----------------------------- |
| `animation-100--all`  | `transition-all duration-100` |
| `animation-300--all`  | `transition-all duration-300` |
| `animation-500--all`  | `transition-all duration-500` |
| `animation-5000--all` | `transition-all` at 5000ms    |



Apply `transition` (Tailwind default properties) with a fixed duration:

| Class            | Transition                 |
| ---------------- | -------------------------- |
| `animation-100`  | `transition duration-100`  |
| `animation-200`  | `transition duration-200`  |
| `animation-300`  | `transition duration-300`  |
| `animation-500`  | `transition duration-500`  |
| `animation-1000` | `transition duration-1000` |
| `animation-5000` | `transition` at 5000ms     |



## Keyframe animations

| Class                 | Effect                                          |
| --------------------- | ----------------------------------------------- |
| `animate-pause`       | Pauses a running CSS animation                  |
| `animate-xscroll`     | Continuous horizontal scroll (10s linear loop)  |
| `animate-widthexpand` | Width expands 0→100% with fade (500ms infinite) |
| `animate-hop1`        | Vertical hop, stagger offset 0.2s               |
| `animate-hop2`        | Vertical hop, stagger offset 0.4s               |
| `animate-hop3`        | Vertical hop, stagger offset 0.6s               |



## Scroll-driven animations

These use `animation-timeline: view()` and require browser support for `animation-range`. Elements animate as they scroll into and out of the viewport within the 10%–90% range. The `@supports` guard means they silently do nothing in unsupported browsers.

| Class                         | Enter / exit effect                |
| ----------------------------- | ---------------------------------- |
| `scroll-fullblurinout-10-90`  | Fade + blur in and out             |
| `scroll-slideupdown-10-90`    | Slide down from above, exit upward |
| `scroll-slidedownup-10-90`    | Slide up from below, exit downward |
| `scroll-slideleftright-10-90` | Slide in from left, exit left      |
| `scroll-sliderightleft-10-90` | Slide in from right, exit right    |
| `scroll-zoominout-10-90`      | Scale up from 80%, fade in         |
