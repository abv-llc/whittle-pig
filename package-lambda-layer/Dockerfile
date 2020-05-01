FROM lambci/lambda:build-python3.7

WORKDIR /var/task
ENV WORKDIR /var/task

# Make the dir and to install all packages into packages/
RUN mkdir -p packages/ && \
    pip install numpy scipy pandas -t packages/

# Copy initial source codes into container.
COPY lambda_handler.py "$WORKDIR/lambda_handler.py"

# Compress all source codes.
# RUN zip -r9 $WORKDIR/lambda.zip packages/ lambda_handler.py

# CMD ["/bin/bash"]
