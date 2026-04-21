renderAdminSocialLinks();
renderAdminArticles();

function renderAdminSocialLinks() {
  const socialLinksContainer = document.getElementById("social-links");

  const items = document.getElementsByClassName('social-link-item')

  Array.from(items).forEach((div, index) => {
    div.innerHTML += `
            <button onclick="editSocialLink(${index})">Edit</button>
            <button onclick="deleteSocialLink(${index})">Delete</button>
        `;
  });
  const addLinkBtn = document.createElement("button");
  addLinkBtn.textContent = "Add Social Link";
  addLinkBtn.onclick = addSocialLink;
  socialLinksContainer.appendChild(addLinkBtn);
}

function renderAdminArticles() {
  const contentDiv = document.querySelector(".content");

  const items = document.getElementsByClassName('article')

  Array.from(items).forEach((articleDiv, index) => {
    const article = articles[index]
    articleDiv.innerHTML = `
            <h2 class="editable-field" onclick="editArticle(${index}, 'title')">${article.title}</h2>
            <p class="editable-field" onclick="editArticle(${index}, 'content')">${article.content}</p>
            <img src="${article.image}" alt="Article Image" class="editable-field" onclick="editArticle(${index}, 'image')">
            <button class="edit-btn" onclick="deleteArticle(${index})">Delete Article</button>
        `;
  });
  const addArticleBtn = document.createElement("button");
  addArticleBtn.textContent = "Add Article";
  addArticleBtn.onclick = addArticle;
  contentDiv.appendChild(addArticleBtn);
}

function saveLogo() {
  const logoUrl = prompt(
    "Enter new logo URL:",
    localStorage.getItem("logo") ||
      "https://taito.edu.turku.fi/pluginfile.php/1/theme_mb2nl/logo/1729438228/tai_logo_300x150.png"
  );
  if (logoUrl) {
    localStorage.setItem("logo", logoUrl);
    document.getElementById("logo").src = logoUrl;
    alert("Logo updated successfully! Refresh index.html to see changes.");
  } else {
    alert("No changes made.");
  }
}

function addLogo() {
  const logoUrl = prompt("Enter new logo URL:");
  if (logoUrl) {
    localStorage.setItem("logo", logoUrl);
    document.getElementById("logo").src = logoUrl;
    alert("Logo added successfully! Refresh index.html to see changes.");
  } else {
    alert("Please enter a URL.");
  }
}

function deleteLogo() {
  if (
    confirm(
      "Are you sure you want to delete the logo? It will revert to default."
    )
  ) {
    localStorage.removeItem("logo");
    document.getElementById("logo").src =
      "https://taito.edu.turku.fi/pluginfile.php/1/theme_mb2nl/logo/1729438228/tai_logo_300x150.png";
    alert("Logo deleted! Refresh index.html to see changes.");
  }
}

function saveFooterNote() {
  const footerNote = prompt(
    "Enter new footer note:",
    localStorage.getItem("footerNote") ||
      "© 2024, Company's name. All rights reserved."
  );
  if (footerNote) {
    localStorage.setItem("footerNote", footerNote);
    document.getElementById("footer-note").textContent = footerNote;
    alert(
      "Footer note updated successfully! Refresh index.html to see changes."
    );
  } else {
    alert("No changes made.");
  }
}

function addFooterNote() {
  const footerNote = prompt("Enter new footer note:");
  if (footerNote) {
    localStorage.setItem("footerNote", footerNote);
    document.getElementById("footer-note").textContent = footerNote;
    alert("Footer note added successfully! Refresh index.html to see changes.");
  } else {
    alert("Please enter a footer note.");
  }
}

function deleteFooterNote() {
  if (
    confirm(
      "Are you sure you want to delete the footer note? It will revert to default."
    )
  ) {
    localStorage.removeItem("footerNote");
    document.getElementById("footer-note").textContent =
      "© 2024, Company's name. All rights reserved.";
    alert("Footer note deleted! Refresh index.html to see changes.");
  }
}

// Add social link
function addSocialLink() {
  const text = prompt("Enter display text for the social link:");
  const url = prompt("Enter URL for the social link:");
  if (text && url) {
    socialLinks.push({ text, url });
    localStorage.setItem("socialLinks", JSON.stringify(socialLinks));
    renderSocialLinks();
    alert("Social link added successfully! Refresh index.html to see changes.");
  } else {
    alert("Both text and URL are required.");
  }
}

function editSocialLink(index) {
  const link = socialLinks[index];
  const newText = prompt("Edit display text:", link.text);
  const newUrl = prompt("Edit URL:", link.url);
  if (newText && newUrl) {
    socialLinks[index] = { text: newText, url: newUrl };
    localStorage.setItem("socialLinks", JSON.stringify(socialLinks));
    renderSocialLinks();
    alert(
      "Social link updated successfully! Refresh index.html to see changes."
    );
  } else {
    alert("Both text and URL are required.");
  }
}

function deleteSocialLink(index) {
  if (confirm("Are you sure you want to delete this social link?")) {
    socialLinks.splice(index, 1);
    localStorage.setItem("socialLinks", JSON.stringify(socialLinks));
    renderSocialLinks();
    alert("Social link deleted! Refresh index.html to see changes.");
  }
}

function editArticle(index, field) {
  let value;
  if (field === "title" || field === "content") {
    value = prompt(`Edit ${field}:`, articles[index][field]);
  } else if (field === "image") {
    value = prompt("Edit image URL:", articles[index][field]);
  }
  if (value !== null) {
    articles[index][field] = value;
    localStorage.setItem("articles", JSON.stringify(articles));
    renderArticles();
    alert(`${field} updated successfully! Refresh index.html to see changes.`);
  }
}

function deleteArticle(index) {
  if (confirm("Are you sure you want to delete this article?")) {
    articles.splice(index, 1);
    localStorage.setItem("articles", JSON.stringify(articles));
    renderArticles();
    alert("Article deleted! Refresh index.html to see changes.");
  }
}

function addArticle() {
  const title = prompt("Enter article title:");
  const content = prompt("Enter article content:");
  const image = prompt("Enter article image URL:");
  if (title && content && image) {
    articles.push({ title, content, image });
    localStorage.setItem("articles", JSON.stringify(articles));
    renderArticles();
    alert("Article added successfully! Refresh index.html to see changes.");
  } else {
    alert("Title, content, and image URL are required.");
  }
}

// Reset all to default
function resetAll() {
  if (
    confirm(
      "Are you sure you want to reset all content to default? This will clear all changes."
    )
  ) {
    localStorage.setItem(
      "logo",
      "https://taito.edu.turku.fi/pluginfile.php/1/theme_mb2nl/logo/1729438228/tai_logo_300x150.png"
    );
    localStorage.setItem(
      "footerNote",
      "© 2024, Company's name. All rights reserved."
    );
    localStorage.setItem(
      "socialLinks",
      JSON.stringify([
        { text: "Facebook", url: "#" },
        { text: "LinkedIn", url: "#" },
        { text: "GitHub", url: "#" },
      ])
    );
    localStorage.setItem(
      "articles",
      JSON.stringify([
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
      ])
    );
    location.reload(); // Reload to apply defaults
    alert("All content reset to default! Refresh index.html to see changes.");
  }
}
