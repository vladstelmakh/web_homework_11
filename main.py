if __name__ == "__main__":
    import uvicorn
    uvicorn.run("endpoints:app", host="127.0.0.1", port=8001, reload=True)
