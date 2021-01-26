FROM openjdk:13-jdk-slim AS build
WORKDIR /app
COPY . /app
RUN ./mvnw install -DskipTests

FROM openjdk:13-jdk-slim

EXPOSE 8080

RUN mkdir /app

COPY --from=build /app/target/*.jar /app/hibernatedemo.jar

ENTRYPOINT ["java","-Dserver.port=8080","-jar","/app/hibernatedemo.jar"]