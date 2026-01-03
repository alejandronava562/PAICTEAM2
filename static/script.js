const usernameInput = document.getElementById("username");
const difficultyButtons = document.querySelectorAll(".difficulty");
const startBtn = document.getElementById("startBtn");
const form = document.getElementById("startForm");
const statusEl = document.getElementById("status");
const game_screen = document.getElementById("game_screen")
const start_screen = document.getElementById("start_screen")
const sceneText = document.getElementById("scene-text");
const bossName = document.getElementById("boss_name")
const player_hp = document.getElementById("player_hp")
const boss_hp = document.getElementById("boss_hp")
const gamestatus = document.getElementById("gameStatus")


let selectedDifficulty = null;

function updateStartButton() {
  const hasUsername = usernameInput.value.trim().length > 0;
  startBtn.disabled = !(hasUsername && selectedDifficulty);
}

function setStatus(message) {
  if (!statusEl) return;
  statusEl.textContent = message ?? "";
}

difficultyButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    difficultyButtons.forEach((b) => {
      b.classList.remove("active");
      b.setAttribute("aria-checked", "false");
    });

    btn.classList.add("active");
    btn.setAttribute("aria-checked", "true");
    selectedDifficulty = btn.dataset.value;

    updateStartButton();
  });
});

usernameInput.addEventListener("input", updateStartButton);

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = usernameInput.value.trim();
  if (!username || !selectedDifficulty) return;

  localStorage.setItem("username", username);
  localStorage.setItem("difficulty", selectedDifficulty);

  startBtn.disabled = true;
  setStatus("Starting game...");

  try {
    const res = await fetch("/api/start", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, difficulty: selectedDifficulty }),
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Start failed (${res.status}): ${text}`);
    }

    const data = await res.json();
    localStorage.setItem("bosses", JSON.stringify(data.bosses ?? []));
    localStorage.setItem("player_hp", data.player_hp ?? "3");
    loadFirstStage();
  } catch (err) {
    console.error(err);
    setStatus("Could not start game. Please try again.");
  } finally {
    updateStartButton();
  }
});

async function loadFirstStage() {
  const bosses = JSON.parse(localStorage.getItem("bosses"));
  if (!bosses.length) {
    setStatus("No bosses found. Please restart.")
    return;
  }
  const bossIndex = 0;
  const response = await fetch("/api/scene", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({boss_index: bossIndex})
  });
  const data = await response.json();
  displayScene(data, bossIndex, bosses[bossIndex])

}

function displayScene(data, bossIndex, boss) {
  start_screen.classList.add("hidden");
  game_screen.classList.remove("hidden");
  game_screen.setAttribute("aria-hidden", "false");
  sceneText.textContent = data.scene;
}