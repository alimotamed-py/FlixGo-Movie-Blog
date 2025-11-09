document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("load-more-btn");
    const postRow = document.getElementById("post-row");

    if (!btn || !postRow) return;

    btn.addEventListener("click", function() {
        const page = parseInt(btn.getAttribute("data-next-page"));

        fetch(`/load-more-posts/?page=${page}`)
        .then(res => res.json())
        .then(data => {
            postRow.insertAdjacentHTML("beforeend", data.html);

            if (data.has_next) {
                btn.setAttribute("data-next-page", page + 1);
            } else {
                btn.style.display = "none";
            }
        })
        .catch(err => console.error(err));
    });
});
