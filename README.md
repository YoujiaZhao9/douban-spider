# 🎬 豆瓣电影 Top250 可视化网站

> 一个从 0 到 1 完成的 Python 全栈练习项目（爬虫 + 数据分析 + Web + 部署）

---

## 🚀 项目简介

本项目通过爬取豆瓣电影 Top250 数据，构建了一个可搜索、可排序、可分页浏览的电影网站。

👉 在线地址：web-production-46b48.up.railway.app

---

## 🖼️ 项目预览

![首页](images/home.png)

![搜索](images/search.png)

![分页](images/page.png)

## ✨ 核心功能

* 🔍 关键词搜索（电影名称）
* ⭐ 评分排序（高 → 低 / 低 → 高）
* 📄 分页加载（每页 10 条）
* 🎬 卡片式电影展示（含封面）
* 🔗 跳转豆瓣详情页
* 🖼️ 图片容错（加载失败自动替换）

---

## 🧠 技术栈

* Python
* Flask
* Pandas
* Requests / BeautifulSoup
* HTML + CSS
* Railway（部署）
* GitHub（版本管理）

---

## 🏗️ 项目结构

```bash
douban-spider/
│
├── app.py              # Flask 后端
├── main.py             # 爬虫脚本
├── analyze.py          # 数据分析
├── movies.csv          # 数据文件
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ 本地运行

```bash
python -m pip install -r requirements.txt
python main.py
python app.py
```

打开浏览器：

```
http://127.0.0.1:5000
```

---

## 🌐 部署说明

项目已部署在 Railway：

1. 上传代码到 GitHub
2. Railway 连接仓库
3. 自动构建并运行 Flask

---

## 🔥 项目亮点（面试加分点）

* 从数据采集 → 数据处理 → Web展示 → 云部署的完整流程
* 实现真实网站常见功能（搜索 / 排序 / 分页）
* 具备前后端联动能力
* 项目结构清晰，易扩展

---

## 🚧 可优化方向

* 电影详情页（单页应用）
* 图片本地化存储（避免外链失效）
* 用户系统（登录 / 收藏）
* 移动端适配
* 接入 AI 推荐功能

---

## 👨‍💻 作者

一个从零开始完成全流程开发的学习项目，用于展示 Python + Web 开发能力。
