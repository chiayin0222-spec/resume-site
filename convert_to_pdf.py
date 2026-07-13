#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import os
from pathlib import Path

async def convert_html_to_pdf():
    """使用 Playwright 將 HTML 轉換為 PDF"""
    from playwright.async_api import async_playwright
    
    # 取得當前目錄
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, 'code_artifact.html')
    pdf_file = os.path.join(current_dir, 'code_artifact.pdf')
    
    if not os.path.exists(html_file):
        print(f"❌ 錯誤：找不到 {html_file}")
        return
    
    print(f"正在轉換 {html_file} 為 PDF...")
    
    async with async_playwright() as p:
        # 啟動 Chromium
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # 加載 HTML 文件
        file_url = Path(html_file).as_uri()
        await page.goto(file_url, wait_until='networkidle')
        
        # 轉換為 PDF（A4 尺寸）
        await page.pdf(path=pdf_file, format='A4', margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        
        await browser.close()
    
    print(f"✓ PDF 已成功產出：{pdf_file}")

# 執行轉換
if __name__ == '__main__':
    asyncio.run(convert_html_to_pdf())
