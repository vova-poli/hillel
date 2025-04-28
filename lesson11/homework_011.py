import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """

    assert isinstance(username, str) and username.strip(), "username має бути непорожнім рядком"
    assert status in ["success", "expired", "failed", "suspicious"], "status має бути одним з дозволених значень"

    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


if __name__ == "__main__":
    log_event("john_doe", "success")
    log_event("jane_doe", "expired")
    log_event("hacker", "failed")
    log_event("bot", "suspicious")
