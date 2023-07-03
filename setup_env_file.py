with open(".env", "w") as f:
    f.write("DJANGO_SECRET_KEY=temp_key \n")
    f.write("SENTRY_DSN=http://none@none/123 \n")
    f.write("HOST_URL=temp_host \n")
    f.close()

print("\n.env file template created!")
