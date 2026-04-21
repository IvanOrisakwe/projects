let articles = JSON.parse(localStorage.getItem("articles")) || [
  {
    title: "A title for your first article",
    content:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    image:
      "https://preview.redd.it/nissan-skyline-gtr-r34-these-are-all-the-photos-wallpapers-v0-2ifr1pr92bue1.jpg?width=640&crop=smart&auto=webp&s=4e7c1f72224a895d4c81cf1340cffe0e0547df56",
  },
  {
    title: "A title for your first article",
    content:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    image:
      "https://preview.redd.it/nissan-skyline-gtr-r34-these-are-all-the-photos-wallpapers-v0-2ifr1pr92bue1.jpg?width=640&crop=smart&auto=webp&s=4e7c1f72224a895d4c81cf1340cffe0e0547df56",
  },
];

let socialLinks = JSON.parse(localStorage.getItem("socialLinks")) || [
  { text: "Facebook", url: "#" },
  { text: "LinkedIn", url: "#" },
  { text: "GitHub", url: "#" },
];

const logo =
  localStorage.getItem("logo") ||
  "https://taito.edu.turku.fi/pluginfile.php/1/theme_mb2nl/logo/1729438228/tai_logo_300x150.png";
document.getElementById("logo").src = logo;
const footerNote =
  localStorage.getItem("footerNote") ||
  "© 2024, Company's name. All rights reserved.";
document.getElementById("footer-note").textContent = footerNote;

renderSocialLinks();
renderArticles();

function renderSocialLinks() {
  const socialLinksContainer = document.getElementById("social-links");
  socialLinksContainer.innerHTML = "";
  socialLinks.forEach((link, index) => {
    const div = document.createElement("div");
    div.className = "social-link-item";
    div.innerHTML = `
            <a href="${link.url}">${link.text}</a>
        `;
    socialLinksContainer.appendChild(div);
  });
}

function renderArticles() {
  const contentDiv = document.querySelector(".content");
  contentDiv.innerHTML = "";
  articles.forEach((article, index) => {
    const articleDiv = document.createElement("div");
    articleDiv.className = "article";
    articleDiv.innerHTML = `
            <h2>${article.title}</h2>
            <p>${article.content}</p>
            <img src="${article.image}" alt="Article Image">
        `;
    contentDiv.appendChild(articleDiv);
  });
}
