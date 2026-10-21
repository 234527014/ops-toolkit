import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("demo.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logging.debug("这条是调试信息,默认看不到")
logging.info("开机检测")
logging.warning("主机8.8.8.8 响应慢")
logging.error("192.0.0.1 不通")