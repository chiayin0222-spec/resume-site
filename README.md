# 陳嘉茵 - 履歷 / 作品展示

此資料夾包含靜態 HTML 履歷與相關圖片檔，適合直接以瀏覽器開啟或部署為靜態網站供人預覽。

## 檔案清單
- `code_artifact.html` - 履歷主頁（可直接用瀏覽器開啟）
- `image_b9d3a1.png` - 個人照片
- 其他 PDF/圖片檔（履歷與截圖）

## 本地預覽
在檔案總管中雙擊 `code_artifact.html` 或於命令列執行：

```powershell
# 開啟預設瀏覽器檢視
Start-Process "./code_artifact.html"
```

## 部署選項（快速）

- GitHub Pages（建議：公開展示、免費）
  1. 在 GitHub 建立新 repository（公開或私有）。
  2. 在本機資料夾初始化 Git 並提交：

```bash
git init
git add .
git commit -m "Add resume site"
git branch -M main
git remote add origin https://github.com/<你的帳號>/<repo>.git
git push -u origin main
```

  3. 在 GitHub 頁面中進入 `Settings` → `Pages`，選擇 `main` branch 並儲存，稍候即可取得 GitHub Pages 網址。

- Netlify（拖放或串接 Git）
  - 將整個資料夾壓縮後於 Netlify 的 Sites 面板使用 `Drag & Drop` 上傳，或串接 GitHub repository 進行部署。

- OneDrive（私人備份或分享）
  - 將整個資料夾上傳至 OneDrive，同步後使用分享連結（需登入帳號）。

- AWS S3 / Azure Blob（進階：大量訪問或加 CDN）
  - 適合高流量或企業級部署，需額外設定 ACL 與 CDN。

## 注意事項
- 本專案為靜態 HTML，若要改名或替換圖片，請確保 `code_artifact.html` 中 `<img>` 的 `src` 對應正確檔名。
- 若需要我幫你把檔案上傳到 GitHub（建立 repo 並推送），請提供 GitHub 帳號名稱，或同意我在本機初始化 Git 並產生推送指令；若要我代為推送，請提供一個 Personal Access Token（或選擇手動操作，我提供步驟）。

---

需要我幫你：
- 直接初始化 Git 並產生推送指令（我會產生命令，你自行執行或提供 token 讓我協助推送）
- 或我幫你把檔案準備好以拖放方式上傳到 Netlify

請告訴我你想部署到哪個平台，我就繼續下一步。
