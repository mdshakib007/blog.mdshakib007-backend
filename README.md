## 📌 Personal Portfolio Blog API Backend  

This is the backend API for the blog section of my personal portfolio. It provides endpoints to retrieve blog posts, interact with posts via claps and comments, and optimize database queries for performance.  

### 🚀 API Endpoints  

| Method | Endpoint | Description |
|--------|-----------------------------|---------------------------|
| `GET` | `/admin/api/v1/` | Admin panel access |
| `GET` | `/api/v1/blog/posts/` | Retrieve all blog posts (paginated) |
| `GET` | `/api/v1/blog/recent-posts/` | Fetch the 3 most recent posts |
| `GET` | `/api/v1/blog/posts/{id}/` | Retrieve a single blog post (optimized) |
| `POST` | `/api/v1/blog/posts/{id}/clap/` | Increase clap count for a post |
| `POST` | `/api/v1/blog/posts/{id}/comments/add/` | Add a comment to a blog post |
| `POST` | `/api/v1/subscription/subscribe/` | Subscribe to get notified when a post published |
| `POST` | `/api/v1/subscription/unsubscribe/{email}/` | Unsubscribe from getting notification |

---

### ⚡ Optimization Strategies  

Since this API is designed for a personal portfolio, authentication is not implemented to keep things lightweight and straightforward. However, several optimizations have been applied to enhance performance:  

- **Efficient Database Queries:**  
  - Reduced unnecessary database calls while ensuring all necessary information is fetched efficiently.  
  - For the **recent posts** endpoint, only the **latest 3 posts** are retrieved instead of fetching excessive data.  

- **Optimized Post Listings:**  
  - When retrieving a list of posts, **comments and full descriptions are excluded** to minimize data load.  
  - Only **image, title, and pagination** are used for fast and efficient data retrieval.  

- **Single Post Optimization:**  
  - When fetching a **detailed blog post**, only **2-3 database queries** are executed to retrieve the post and its **5 most recent comments** using `select_related`.  

- **Clap Feature:**  
  - The **clap counter** is updated via a lightweight API call, avoiding unnecessary overhead.  

- **Comments System:**  
  - Users can submit a comment with just their **name** and **comment body**, ensuring a simple and seamless interaction.  

- **Subscription System:**  
  - Users can subscribe to get email **notified** when a new blog-post published, also simply can unsubscribe.  

---

### 📌 Technologies Used  

- **Django REST Framework (DRF)** – For building RESTful API endpoints.  
- **PostgreSQL** – As the database.  
- **Pagination & Query Optimization** – For efficient data fetching.  