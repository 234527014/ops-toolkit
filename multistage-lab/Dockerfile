FROM alpine AS builder
RUN apk add --no-cache build-base
COPY hello.sh /hello.sh
RUN chmod +x /hello.sh

FROM alpine
COPY --from=builder /hello.sh /hello.sh
ENTRYPOINT [ "/hello.sh" ]