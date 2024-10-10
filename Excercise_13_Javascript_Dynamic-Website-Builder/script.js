var count = 0;

function createCard(title, channel, views, monthOld, duration, thumbnail) {
    count += 1;
    if (views >= 1000 & views < 1000000) {
        viewsStr = Math.round(views / 1000) + "K"
    }
    else if (views >= 1000000) {
        viewsStr = Math.round(views / 1000000) + "M"
    }
    else {
        viewsStr = views
    }


    let card = document.createElement("div");
    card.setAttribute("class", "card");
    card.innerHTML = `<div class="srno">${count}</div>
            <div class="video">
                <img src=${thumbnail}>
                <div class="duration">${duration}</div>
            </div>
            <div class="details">
                <div class="title">${title}</div>
                <div class="description">
                    <span class="channel">${channel}</span><span>•</span>
                    <span class="views">${viewsStr}</span><span>•</span>
                    <span class="monthOld">${monthOld}</span>
                </div>
            </div>`;
    document.querySelector(".container").append(card);
}
createCard("Bhool Bhulaiyaa 3 (Official Trailer): Kartik Aaryan,Vidya B,Madhuri D,Triptii | Anees B | Bhushan K", "T Series", 53142, "1 day ago", "3:51", "https://i.ytimg.com/vi/6YMY62tMLUA/hq720.jpg")
createCard("Bhool Bhulaiyaa 3 (Official Trailer): Kartik Aaryan,Vidya B,Madhuri D,Triptii | Anees B | Bhushan K", "T Series", 52230742, "1 day ago", "3:51", "https://i.ytimg.com/vi/MD7v0-igVIM/hq720.jpg")