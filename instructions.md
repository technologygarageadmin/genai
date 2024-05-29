aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com

docker build -t my-genai-app .

docker tag my-genai-app:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-genai-app:latest
docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-genai-app:latest

docker tag my-genai-app my-genai-app:latest
 