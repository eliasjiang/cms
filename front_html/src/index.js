import './main.css';
import './index.css'
// import Swiper bundle with all modules installed
import Swiper from 'swiper/bundle';

// import styles bundle
import 'swiper/css/bundle';


function siblingElems(elem) {
  var nodes = [];

  var _elem = elem;

  while ((elem = elem.previousSibling)) {
    if (elem.nodeType == 1) {
      nodes.push(elem);
    }
  }

  var elem = _elem;

  while ((elem = elem.nextSibling)) {
    if (elem.nodeType == 1) {
      nodes.push(elem);
    }
  }

}


const groups = document.getElementsByClassName(".index_group");
const timer = setTimeout(function () {
  for (let i = 0, n = groups.length; i < n; i++) {
    groups[i].style.zIndex = 10;
  }
}, 2000);


const mySwiper = new Swiper("#full-width-slider", {
  // simulateTouch : false,
  // onlyExternal:true,
  // mousewheelControl : true,
  resistance: "100%",
  onSlideChangeEnd: function (mySwiper) {
    // 
    var charmaIndex = parseInt(mySwiper.activeIndex);
    const mimgs = document.querySelectorAll(".index_mouse img")
    console.dir(charmaIndex);
    if (charmaIndex == 1) {

      const mSpan = document.querySelector(".index_mouse span:nth-child(2)")
      mSpan.classList.add("bullet-active");

      const nSpans = siblingElems(mSpan);

      for (let k = 0, u = nSpans.length; k < u; k++) {
        nSpans[k].classList.remove("bullet-active");
      }

      for (let i = 0, n = mimgs.length; i < n; i++) {
        mimgs[k].setAttribute("src", "assets/images/index_left_arrow.png");
      }

    } else if (charmaIndex == 0) {

      const mSpan = document.querySelector(".index_mouse span:nth-child(1)")
      mSpan.classList.add("bullet-active");

      const nSpans = siblingElems(mSpan);

      for (let k = 0, u = nSpans.length; k < u; k++) {
        nSpans[k].classList.remove("bullet-active");
      }

      for (let i = 0, n = mimgs.length; i < n; i++) {
        mimgs[k].setAttribute("src", "assets/images/index_right_arrow.png");
      }
    }
  },
});



const mimgs = document.querySelectorAll(".index_mouse img")

for (let i = 0, n = mimgs.length; i < n; i++) {
  mimgs[i].addEventListener('click', () => {
    const img = mimgs[i].getAttribute("src");

    if (img === "assets/images/index_left_arrow.png") {
      mySwiper.slideTo(0, 500, false);
      for (let k = 0; k < n; k++) {
        mimgs[k].setAttribute("src", "assets/images/index_right_arrow.png");
      }
    } else {
      mySwiper.slideTo(1, 500, false);
      for (let k = 0; k < n; k++) {
        mimgs[k].setAttribute("src", "assets/images/index_left_arrow.png");
      }
    }
  });
}

const mSpans = document.querySelectorAll(".index_mouse span")

for (let i = 0, n = mSpans.length; i < n; i++) {
  const nSpans = siblingElems(mSpans[i]);
  mSpans[i].addEventListener('click', () => {
    mSpans[i].classList.add("bullet-active");

  });
  for (let k = 0, u = nSpans.length; k < u; k++) {
    nSpans[k].classList.remove("bullet-active");
  }
}
