<<<<<<< HEAD
# NLP-Project---News-Classification

## 1. Mục tiêu dự án
### 1.1. Mô tả mục tiêu
Xây dựng một hệ thống phân loại tin tức tiếng Việt dựa trên các mô hình ngôn ngữ pre-trained thông qua kỹ thuật fine-tuning. Mô hình đầu ra có khả năng gán nhãn chủ đề phù hợp cho mỗi bài báo như Thời sự, Thể thao, Giáo dục, Sức khỏe, Giải trí, v.v.

### 1.2. Công nghệ sử dụng:
- Ngôn ngữ: Python
- Thư viện NLP: transformers, datasets, torch, underthesea, VnCoreNLP
- Tiền xử lý & crawl: BeautifulSoup, Selenium, re, unicodedata
- Huấn luyện mô hình: PyTorch, Hugging Face Transformers
- Đánh giá mô hình: scikit-learn, matplotlib, seaborn (vẽ confusion matrix)
- Triển khai hệ thống gợi ý (nếu có): FAISS, Redis, Flask hoặc FastAPI


## 2. Các bước thực hiện
1. Thu thập dữ liệu
- Thu thập dữ liệu dạng văn bản từ trang web: https://vtv.vn/
- Dữ liệu đầu ra: file .json gồm các trường title, category, article, news_link, short_description, content.
- Sử dụng BeautifulSoup, Selenium để thu thập tự động.

2. Tiền xử lý dữ liệu
- Loại bỏ HTML tag, ký tự đặc biệt, nội dung quảng cáo, watermark.
- Ghép title + content thành một trường duy nhất để phục vụ huấn luyện.
- Chuyển văn bản về dạng chữ thường, chuẩn hóa Unicode.
- Loại bỏ các bài viết trùng lặp, bài quá ngắn, bài không có nhãn rõ ràng.

3. Tách từ (tokenization)
- Thử nghiệm một số tool dựa vào mô hình fine-tune:
    - vinai/phobert-base: WordPiece tokenizer
    - nguyenvulebinh/vi-mrc-base: SentencePiece tokenizer
    - Sử dụng AutoTokenizer từ thư viện Transformers để tự động tải tokenizer phù hợp với mô hình được chọn.

4. Chuẩn bị tập dữ liệu huấn luyện
- Chia dữ liệu theo tỷ lệ: Train / Validation / Test = 80 / 10 / 10.
- Encode văn bản và nhãn thành tensor (input_ids, attention_mask, labels).

5. Huấn luyện mô hình
- Chọn mô hình pre-trained tiếng Việt (gợi ý):
    - vinai/phobert-base
    - nguyenvulebinh/vi-mrc-base
- Dùng thư viện Transformers của Hugging Face.
- Cấu hình huấn luyện:
    - Optimizer: AdamW
    - Loss: CrossEntropyLoss
    - Learning rate scheduler, early stopping
    - Evaluation mỗi epoch

6. Đánh giá mô hình
- Sử dụng các metric: Accuracy, Precision, Recall, F1-score (macro/micro)
- Hiển thị confusion matrix để phân tích lỗi.
- Kiểm tra với tập test chưa thấy trong quá trình huấn luyện.
- Lưu lại mô hình tốt nhất theo metric F1-score trên tập validation.


## 3. Kế hoạch mở rộng
Sau khi xây dựng thành công mô hình phân loại báo, dự án sẽ được mở rộng theo hướng xây dựng hệ thống gợi ý bài viết tương tự (content-based recommendation) bằng cách khai thác sức mạnh của các mô hình ngôn ngữ lớn (LLM).

### 3.1. Mục tiêu:
Gợi ý các bài báo liên quan/dễ đọc tiếp theo dựa trên nội dung bài hiện tại.

### 3.2. Hướng tiếp cận:
1. Sinh vector embedding cho mỗi bài báo:
- Dùng mô hình pre-trained hoặc LLM như vinai/phobert-base, sentence-transformers, hoặc bactrian-x/vietnamese-sbert.
- Áp dụng lên title + content để lấy embedding có ngữ nghĩa.

2. Tính toán độ tương đồng:
- Sử dụng cosine similarity giữa các vector embedding.
- Với mỗi bài báo, truy xuất top-k bài có cosine similarity cao nhất.

3. Triển khai hệ thống gợi ý:
- Kết hợp với Redis, FAISS hoặc Annoy để tăng tốc tìm kiếm vector tương tự trong tập dữ liệu lớn.
- Tích hợp vào ứng dụng web demo hoặc API.

=======
# NLP-Project---News-Classification

## 1. Mục tiêu dự án
### 1.1. Mô tả mục tiêu
Xây dựng một hệ thống phân loại tin tức tiếng Việt dựa trên các mô hình ngôn ngữ pre-trained thông qua kỹ thuật fine-tuning. Mô hình đầu ra có khả năng gán nhãn chủ đề phù hợp cho mỗi bài báo như Thời sự, Thể thao, Giáo dục, Sức khỏe, Giải trí, v.v.

### 1.2. Công nghệ sử dụng:
- Ngôn ngữ: Python
- Thư viện NLP: transformers, datasets, torch, underthesea, VnCoreNLP
- Tiền xử lý & crawl: BeautifulSoup, Selenium, re, unicodedata
- Huấn luyện mô hình: PyTorch, Hugging Face Transformers
- Đánh giá mô hình: scikit-learn, matplotlib, seaborn (vẽ confusion matrix)
- Triển khai hệ thống gợi ý (nếu có): FAISS, Redis, Flask hoặc FastAPI


## 2. Các bước thực hiện
1. Thu thập dữ liệu
- Thu thập dữ liệu dạng văn bản từ trang web: https://vtv.vn/
- Dữ liệu đầu ra: file .json gồm các trường title, category, article, news_link, short_description, content.
- Sử dụng BeautifulSoup, Selenium để thu thập tự động.

2. Tiền xử lý dữ liệu
- Loại bỏ HTML tag, ký tự đặc biệt, nội dung quảng cáo, watermark.
- Ghép title + content thành một trường duy nhất để phục vụ huấn luyện.
- Chuyển văn bản về dạng chữ thường, chuẩn hóa Unicode.
- Loại bỏ các bài viết trùng lặp, bài quá ngắn, bài không có nhãn rõ ràng.

3. Tách từ (tokenization)
- Thử nghiệm một số tool dựa vào mô hình fine-tune:
    - vinai/phobert-base: WordPiece tokenizer
    - nguyenvulebinh/vi-mrc-base: SentencePiece tokenizer
    - Sử dụng AutoTokenizer từ thư viện Transformers để tự động tải tokenizer phù hợp với mô hình được chọn.

4. Chuẩn bị tập dữ liệu huấn luyện
- Chia dữ liệu theo tỷ lệ: Train / Validation / Test = 80 / 10 / 10.
- Encode văn bản và nhãn thành tensor (input_ids, attention_mask, labels).

5. Huấn luyện mô hình
- Chọn mô hình pre-trained tiếng Việt (gợi ý):
    - vinai/phobert-base
    - nguyenvulebinh/vi-mrc-base
- Dùng thư viện Transformers của Hugging Face.
- Cấu hình huấn luyện:
    - Optimizer: AdamW
    - Loss: CrossEntropyLoss
    - Learning rate scheduler, early stopping
    - Evaluation mỗi epoch

6. Đánh giá mô hình
- Sử dụng các metric: Accuracy, Precision, Recall, F1-score (macro/micro)
- Hiển thị confusion matrix để phân tích lỗi.
- Kiểm tra với tập test chưa thấy trong quá trình huấn luyện.
- Lưu lại mô hình tốt nhất theo metric F1-score trên tập validation.


## 3. Kế hoạch mở rộng
Sau khi xây dựng thành công mô hình phân loại báo, dự án sẽ được mở rộng theo hướng xây dựng hệ thống gợi ý bài viết tương tự (content-based recommendation) bằng cách khai thác sức mạnh của các mô hình ngôn ngữ lớn (LLM).

### 3.1. Mục tiêu:
Gợi ý các bài báo liên quan/dễ đọc tiếp theo dựa trên nội dung bài hiện tại.

### 3.2. Hướng tiếp cận:
1. Sinh vector embedding cho mỗi bài báo:
- Dùng mô hình pre-trained hoặc LLM như vinai/phobert-base, sentence-transformers, hoặc bactrian-x/vietnamese-sbert.
- Áp dụng lên title + content để lấy embedding có ngữ nghĩa.

2. Tính toán độ tương đồng:
- Sử dụng cosine similarity giữa các vector embedding.
- Với mỗi bài báo, truy xuất top-k bài có cosine similarity cao nhất.

3. Triển khai hệ thống gợi ý:
- Kết hợp với Redis, FAISS hoặc Annoy để tăng tốc tìm kiếm vector tương tự trong tập dữ liệu lớn.
- Tích hợp vào ứng dụng web demo hoặc API.

>>>>>>> bd3f4a2ae46f6f7b854267b85baf9ff5292a74ac
