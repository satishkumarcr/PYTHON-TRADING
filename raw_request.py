# Example: raw IG API request for IG DEMO
from trading_ig import IGService
from Ig_config_demo import Config

if __name__ == "__main__":
    Config.validate()
    ig_service = IGService(Config.username, Config.password, Config.api_key, Config.acc_type)
    ig_service.create_session()
    # Add your raw request logic here
    print("IGService session created (DEMO)")
