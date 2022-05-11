let starsContainer = document.getElementById("stars")
let active = -1


for (let i = 0; i < 5; i++) {
    let starImg = document.createElement("img");
    starImg.src = "../static/js/star.svg";
    starImg.className = "star-style";
    // let testText = document.createElement("p");
    // testText.innerText = "here I am";
    starsContainer.appendChild(starImg);

    starImg.addEventListener("mouseover", () => onStarHover(i));
    starImg.addEventListener("mouseleave", () => onStarOut(i));
    starImg.addEventListener("click", () => onStarClick(i))
}

let stars = document.querySelectorAll(".star-style")

function onStarHover(i) {
    fill(i)
}

function fill(ratingValue) {
    for (let i = 0; i < 5; i++) {
        if (i <= ratingValue) {
            stars[i].src = "../static/js/starcolored.svg"
        } else {
            stars[i].src = "../static/js/star.svg"
        }
    }
}

function onStarOut(i) {
    fill(active)
}

function onStarClick(i) {
    active = i
    document.getElementById("display-star-value").innerHTML = i + 1
    fill(active)
}
